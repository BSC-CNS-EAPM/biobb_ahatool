from biobb_ahatool.ahatool.ahatool import ahatool


def main():
    prop = {
        "threads": 2,
        "database": "/home/albertcs/GitHub/EAPM/biobb_ahatool/biobb_ahatool/test/data/ahatool/nr_test.fa",
        "binary_path": "/home/albertcs/Projects/WP2/Containers/HMM/AHATool/AHATool.sh",
        'support_folder': "/home/albertcs/Projects/WP2/Containers/HMM/AHATool/AHATool_Resources/",
        "remove_tmp": False
    }

    rcode = ahatool(input_path="/home/albertcs/GitHub/EAPM/biobb_ahatool/biobb_ahatool/test/data/ahatool/test.fasta",
                    output_path="/home/albertcs/GitHub/EAPM/biobb_ahatool/biobb_ahatool/test/data/ahatool/output.zip",
                    properties=prop)


if __name__ == '__main__':
    main()