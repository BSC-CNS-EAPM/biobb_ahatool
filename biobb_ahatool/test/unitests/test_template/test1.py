from biobb_ahatool.ahatool.ahatool import Ahatool


def main():
    prop = {
        "threads": 2,
        "database": "biobb_ahatool/test/data/ahatool/nr_test.fa",
        "binary_path": "/home/albertcs/GitHub/EAPM/AHATool-container/AHATool.sh",
        "remove_tmp": False
    }

    rcode = Ahatool(input_path="biobb_ahatool/test/data/ahatool/test.fa", output_path="biobb_ahatool/test/data/ahatool/output.zip", properties=properties)


if __name__ == '__main__':
    main()