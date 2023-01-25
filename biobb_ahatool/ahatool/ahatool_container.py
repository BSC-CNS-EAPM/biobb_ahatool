#!/usr/bin/env python3

"""Module containing the TemplateContainer class and the command line interface."""
import argparse
import os
from pathlib import Path

from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger


# 1. Rename class as required
class AhatoolContainer(BiobbObject):
    """
    | biobb_ahatool AHATool
    | Wrapper of the AHATool module.
    | AHATool an Automatic HMM and Analysis Tool.

    Args:
        input_path (str): Path to the input file. File type: input. Accepted formats: FASTA (edam:format_1929), fasta (edam:format_1929),HMM (edam:format_2075), ALN (edam:format_1391).
        output_path (str): Path to the output file. File type: output. Accepted formats: zip (edam:format_3987).
        properties (dic):
            * **prefix** (*str*) - ('yyddmmhhmm') The prefix the tool will use for produced files.
            * **start** (*str*) - ('build') Start of execution (search or build).
            * **binary_path** (*str*) - ("../AHATools/AHATool.sh") Example of executable binary property.
            * **database** (*str*) - ('./nr.fa') Database options: 1. nr_db; 2. custom_db. Path to the database.
            * **evalue** (*float*) - (0.0000000001) e-value (recommended: 1e-10).
            * **threads** (*int*) - (2) Processors options: 1, 2, 4.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **container_path** (*str*) - (docker) Container path definition.
            * **container_image** (*str*) - ('bsceapm/ahatool:X.X') Container image definition.
            * **container_volume_path** (*str*) - ('/home/projects') Container volume path definition.
            * **container_working_dir** (*str*) - ('/home/projects') Container working directory definition.
            * **container_user_id** (*str*) - (None) Container user_id definition.
            * **container_shell_path** (*str*) - ('/bin/bash') Path to default shell inside the container.
    Examples:
        This is a use example of how to use the building block from Python::
            from biobb_ahatool.ahatool.ahatool_container import aahtool_container
            prop = {
                'threads': 4,
                'database': '/database/nr.fa',
                'container_path': 'docker',
                'container_image': 'bsceapm/ahatool:X.X',
                'container_volume_path': '/home/projects'
            }
            aahtool_container(input_path='/path/to/my.fasta',
                            output_file_path='/path/to/newCompressedFile.zip',
                            properties=prop)
    Info:
        * wrapped_software:
            * name: AHATool
            * version: >=1.0
            * license: BSD 3-Clause
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl
    """

    # 2. Adapt input and output file paths as required. Include all files, even optional ones
    def __init__(self, input_path, output_path, properties=None, **kwargs) -> None:
        properties = properties or {}

        # 2.0 Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # 2.1 Modify to match constructor parameters
        # Input/Output files
        self.io_dict = {
            'in': {'input_file_path1': input_path},
            'out': {'output_file_path': output_path}
        }

        # 3. Include all relevant properties here as
        # Properties specific for BB
        self.prefix = properties.get('prefix', None)
        self.start = properties.get('start', None)
        self.database = properties.get('database', None)
        self.evalue = properties.get('evalue', None)
        self.threads = properties.get('threads', None)
        self.binary_path = properties.get('binary_path', '../AHATools/AHATool.sh')
        self.container_volume_path = properties.get('container_volume_path', '/home/projects')
        self.database_folder = properties.get('database_folder', os.getcwd())
        self.container_path = properties.get('container_path', 'docker')
        self.properties = properties

        # Check the properties
        self.check_properties(properties)
        # Check the arguments
        self.check_arguments()

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`TemplateContainer <template.template_container.TemplateContainer>` object."""

        # 4. Setup Biobb
        if self.check_restart(): return 0
        self.stage_files()

        # Creating temporary folder
        self.tmp_folder = fu.create_unique_dir()
        fu.log('Creating %s temporary folder' % self.tmp_folder, self.out_log)

        # 5. Prepare the command line parameters as instructions list
        instructions = []
        if self.prefix:
            instructions.append(f'-p {self.prefix}')
            fu.log('Appending optional prefix', self.out_log, self.global_log)
        if self.start:
            instructions.append(f'-s {self.start}')
            fu.log('Appending optional start', self.out_log, self.global_log)
        if self.database:
            if not os.path.basename(self.database) == 'nr.fa':
                instructions.append(f'-d /home/database/{os.path.basename(self.database)}')
                pathdb = Path(self.database).parent
                self.container_generic_command = f"run -v {pathdb}:/home/database"
                fu.log('Appending optional database', self.out_log, self.global_log)
        if self.evalue:
            instructions.append(f'-e {self.evalue}')
            fu.log('Appending optional evalue', self.out_log, self.global_log)
        if self.threads:
            instructions.append(f'-t {self.threads}')
            fu.log('Appending optional threads', self.out_log, self.global_log)

        # 6. Build the actual command line as a list of items (elements order will be maintained)
        self.cmd = [self.binary_path,
                    ' '.join(instructions),
                    self.stage_io_dict['out']['output_path'],
                    self.stage_io_dict['in']['input_path']]
        fu.log('Creating command line with instructions and required arguments', self.out_log, self.global_log)

        # 8. Uncomment to check the command line
        print(' '.join(self.cmd))

        # Run Biobb block
        self.run_biobb()

        # Copy files to host
        self.copy_to_host()

        # Remove temporary file(s)
        self.tmp_files.extend([
            self.stage_io_dict.get("unique_dir"),
            self.tmp_folder
        ])
        self.remove_tmp_files()

        # Check output arguments
        self.check_arguments(output_files_created=True, raise_exception=False)

        return self.return_code


def ahatool_container(input_path: str, output_path: str,
                       properties: dict = None, **kwargs) -> int:
    """Create :class:`TemplateContainer <template.template_container.TemplateContainer>` class and
    execute the :meth:`launch() <template.template_container.TemplateContainer.launch>` method."""

    return AhatoolContainer(input_path=input_path,
                             output_path=output_path,
                             properties=properties, **kwargs).launch()


def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description='Description for the template container module.',
                                     formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')

    # 10. Include specific args of each building block following the examples. They should match step 2
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_path', required=True,
                               help='Description for the first input file path. Accepted formats: top.')
    required_args.add_argument('--output_path', required=True,
                               help='Description for the output file path. Accepted formats: zip.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    # 11. Adapt to match Class constructor (step 2)
    # Specific call of each building block
    ahatool_container(input_path1=args.input_path,
                       output_path=args.output_file_path,
                       properties=properties)


if __name__ == '__main__':
    main()

# 13. Complete documentation strings
