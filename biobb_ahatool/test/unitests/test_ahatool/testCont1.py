from biobb_ahatool.ahatool.ahatool_container import ahatool_container


def main():
    prop = {
        "threads": 2,
        "database": "/home/albertcs/GitHub/EAPM/biobb_ahatool/biobb_ahatool/test/data/ahatool/nr_test.fa",
        "remove_tmp": False,
        "container_image": "ahatool"
    }

    rcode = ahatool_container(
        input_path="/home/albertcs/GitHub/EAPM/biobb_ahatool/biobb_ahatool/test/data/ahatool/Hyaluronidase_1.hmm",
        output_path="/home/albertcs/GitHub/EAPM/biobb_ahatool/biobb_ahatool/test/data/ahatool/output.zip",
        properties=prop)


if __name__ == '__main__':
    main()
