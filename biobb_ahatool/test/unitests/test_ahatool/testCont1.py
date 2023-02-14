from biobb_ahatool.ahatool.ahatool_container import ahatool_container


def main():
    prop = {
        "threads": 2,
        "database": "/home/albertcs/GitHub/EAPM/biobb_ahatool/biobb_ahatool/test/data/ahatool/nr_test.fa",
        "remove_tmp": False,
        "container_image": "bsceapm/ahatool:1.9"
    }

    rcode = ahatool_container(
        input_path="/home/albertcs/GitHub/EAPM/biobb_ahatool/biobb_ahatool/test/data/ahatool/test.fasta",
        output_path="/home/albertcs/GitHub/EAPM/biobb_ahatool/biobb_ahatool/test/data/ahatool/output.zip",
        properties=prop)


if __name__ == '__main__':
    main()
