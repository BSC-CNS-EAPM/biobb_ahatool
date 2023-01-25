# biobb_ahatool

## Introduction
AHATool an Automatic HMM and Analysis Tool.
This solution connects the process of creating a
multiple sequence alignment (MSA) of selected enzymes with a profile Hidden-Markov
Model (HMM) search against a given database with following biological classification
and characterization of promising enzymes.
[latest API documentation](http://biobb_ahatool.readthedocs.io/en/latest/).

## Version
v0.1.0 2023.1

## Installation

If you have no experience with anaconda, please first take a look to the [New with anaconda?](https://biobb-documentation.readthedocs.io/en/latest/first_steps.html#new-with-anaconda) section of the [official documentation](https://biobb-documentation.readthedocs.io/en/latest/).


### Create new conda environment

Once you have the project unzipped in your computer, please follow the next steps to create a new conda environment:

```console
cd biobb_ahatool-master
conda env create -f conda_env/environment.yml
```

### Update environment paths

Edit **conda_env/biobb_ahatool.pth** with the paths to your *biobb_ahatool* folder. Example:

```console
/home/user_name/projects/biobb_ahatool/
/home/user_name/projects/biobb_ahatool/biobb_ahatool/biobb_ahatool
```

Copy the edited **conda_env/biobb_aahtool.pth** file to the site-packages folder of your environment. This folder is in */[anaconda-path]/envs/biobb_ahatool/lib/python3.7/site-packages*, where */[anaconda-path]* is usually */anaconda3* or */opt/conda*.

```console
cp conda_env/biobb_aahtool.pth /[anaconda-path]/envs/biobb_ahatool/lib/python3.7/site-packages
```

### Activate environment

Then, activate the recently created *biobb_ahatool* conda environment:

```console
conda activate biobb_ahatool
```

### Create repository

This template includes some folders not standard for a biobb, such as **biobb_ahatool/adapters/**, **biobb_ahatool/notebooks/** or **conda_env/**. For the sake of having a pure biobb structure, you should uncomment the three last lines of the **.gitignore** file before creating a new git repository:

```console
biobb_ahatool/adapters
biobb_ahatool/notebooks
conda_env
```
Then, inialitize repository:

```console
git init
```

### Binary paths configuration

Additionally, it's recommendable to configure binary paths in your environment in order to ease the command line execution. More info about this subject in the [Binary path configuration](https://biobb-documentation.readthedocs.io/en/latest/execution.html#binary-path-configuration) section of the [official documentation](https://biobb-documentation.readthedocs.io/en/latest/).

## Run tests

To run tests, please execute the following instruction:

```console
pytest /path/to/biobb_ahatool/biobb_ahatool/test/unitests/test_template/test_template.py
```
Or, if you prefer to show the BioBB output during the test process:

```console
pytest -s /path/to/biobb_ahatool/biobb_ahatool/test/unitests/test_template/test_template.py
```

## Documentation

[Click here to find the API Documentation example](https://biobb-ahatool.readthedocs.io/en/latest/template.html) for this template and [here for Command Line documentation](http://biobb_aahtool.readthedocs.io/en/latest/command_line.html).

And here you can find [the full documentation](https://biobb-documentation.readthedocs.io/en/latest/) about how to build a new **BioExcel building block** from scratch.

## Copyright & Licensing
This software has been developed in the [MMB group](http://mmb.irbbarcelona.org) at the [BSC](http://www.bsc.es/) & [IRB](https://www.irbbarcelona.org/) for the [European BioExcel](http://bioexcel.eu/), funded by the European Commission (EU H2020 [823830](http://cordis.europa.eu/projects/823830), EU H2020 [675728](http://cordis.europa.eu/projects/675728)).

* (c) 2015-2022 [Barcelona Supercomputing Center](https://www.bsc.es/)
* (c) 2015-2022 [Institute for Research in Biomedicine](https://www.irbbarcelona.org/)

Licensed under the
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0), see the file LICENSE for details.

![](https://bioexcel.eu/wp-content/uploads/2019/04/Bioexcell_logo_1080px_transp.png "Bioexcel")
