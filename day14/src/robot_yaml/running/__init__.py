def get_config_and_testcases(src):

    from robot_yaml.datas.yaml_fields import CONFIG, TESTCASES

    if not src:
        raise Exception("yaml contents was None")

    try:
        return src[CONFIG], src[TESTCASES]
    except KeyError as ke:
        raise Exception("yaml file must have config and testcases node")
    except Exception as e:
        raise e
