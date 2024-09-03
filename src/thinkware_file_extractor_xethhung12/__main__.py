import argparse
import json
import sys
from thinkware_file_extractor_xethhung12.script_gen import gen_merge_script

import thinkware_file_extractor_xethhung12 as thinkwareExtractor


def main():
    parser = argparse.ArgumentParser(
        prog='thinkware_file_extractor_xethhung12',
        description='extract thinkware data',
    )

    level_1_subparser=parser.add_subparsers(help="utils", dest="level1")
    level_1_subparser_utils_parser = level_1_subparser.add_parser(
        "utils", description="utils"
    )
    utils_parser_level_2=level_1_subparser_utils_parser.add_subparsers(help="when-x", dest="level2")

    utils_parser_level_2_when_x=utils_parser_level_2.add_parser("when-x")
    utils_parser_level_2_when_x.add_argument(
        "--value","-v", type=str, help="x value"
    )

    utils_parser_level_2_when_x=utils_parser_level_2.add_parser("when-y")
    utils_parser_level_2_when_x.add_argument(
        "--value","-v", type=str, help="y value"
    )

    utils_parser_level_2_scale=utils_parser_level_2.add_parser("scale")
    utils_parser_level_2_scale.add_argument(
        "--value","-v", type=str, help="scale value"
    )

    level_1_subparser_mp4_parser = level_1_subparser.add_parser(
        "mp4", description="mp4 related"
    )
    level_1_subparser_mp4_parser_level_2 = level_1_subparser_mp4_parser.add_subparsers(help="mp4 related", dest="level2")
    level_1_subparser_mp4_parser_level_2_all_parser=level_1_subparser_mp4_parser_level_2.add_parser("all")
    level_1_subparser_mp4_parser_level_2_all_parser.add_argument(
        "--file-name","-f", type=str, help="view file"
    )

    level_1_subparser_mp4_parser_level_2_width_parser=level_1_subparser_mp4_parser_level_2.add_parser("width")
    level_1_subparser_mp4_parser_level_2_width_parser.add_argument(
        "--file-name","-f", type=str, help="view file"
    )

    level_1_subparser_mp4_parser_level_2_height_parser=level_1_subparser_mp4_parser_level_2.add_parser("height")
    level_1_subparser_mp4_parser_level_2_height_parser.add_argument(
        "--file-name","-f", type=str, help="view file"
    )

    level_1_subparser_mp4_parser_level_2_codec_parser=level_1_subparser_mp4_parser_level_2.add_parser("codec")
    level_1_subparser_mp4_parser_level_2_codec_parser.add_argument(
        "--file-name","-f", type=str, help="view file"
    )

    level_1_subparser_script_gen_parser = level_1_subparser.add_parser(
        "script-gen", description="generate scripts"
    )
    level_1_subparser_script_gen_parser_level_2=level_1_subparser_script_gen_parser.add_subparsers(help="merge-script", dest="level2")
    level_1_subparser_script_gen_parser_level_2_parser=level_1_subparser_script_gen_parser_level_2.add_parser("merge-script")
    level_1_subparser_script_gen_parser_level_2_parser.add_argument(
        "--source", type=str, help="source path"
    )
    level_1_subparser_script_gen_parser_level_2_parser.add_argument(
        "--dest", type=str, help="destination path"
    )
    level_1_subparser_script_gen_parser_level_2_parser.add_argument(
        "--prefix", type=str, help="prefix of file", choices = ["EVT", "REC"]
    )
    level_1_subparser_script_gen_parser_level_2_parser.add_argument(
        "--mode", type=str, help="front or rear", choices = ["F", "R"]
    )

    x = parser.parse_args(sys.argv[1:])
    if x.level1 == "utils":
        if(x.level2 == "when-x"):
            val = x.value
            return print(thinkwareExtractor.utils.get_x(val))
        elif x.level2 == "when-y":
            val = x.value
            return print(thinkwareExtractor.utils.get_y(val))
        elif x.level2 == "scale":
            val = x.value
            return print(thinkwareExtractor.utils.get_scale(val))
        else:
            print(x)
    elif x.level1 == "mp4":
        if x.level2 == "all":
            print(json.dumps(thinkwareExtractor.utils_tools.mp4view(x.file_name).map, indent=2))
        elif x.level2 == "width":
            print(thinkwareExtractor.utils_tools.mp4view(x.file_name).get_width())
        elif x.level2 == "height":
            print(thinkwareExtractor.utils_tools.mp4view(x.file_name).get_height())
        elif x.level2 == "codec":
            print(thinkwareExtractor.utils_tools.mp4view(x.file_name).get_codec())
        else:
            print(x)
    elif x.level1 == "script-gen":
        if x.level2 == "merge-script":
            print(gen_merge_script(x.source, x.dest, x.prefix, x.mode))
    else:
        print(x)


if __name__ == '__main__':
    main()
