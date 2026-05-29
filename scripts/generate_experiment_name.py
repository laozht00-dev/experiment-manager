#!/usr/bin/env python3
"""
实验文件名生成器
根据标准实验记录命名规则生成标准化实验文件名
格式：YYMMDD_PROJECT_TARGET_MARKER_ASSAYTYPE_STAGEBATCH
"""

import sys
from datetime import datetime


def generate_experiment_name(date_str, project, target, marker, assay_type, stage_batch):
    """
    生成标准化的实验文件名

    Args:
        date_str: 日期字符串 (YYYY-MM-DD)
        project: 项目代号 (如 PRJ, PRJ2, PRJ3)
        target: 实验对象 (如 SAMPLE_B, SAMPLE_C)
        marker: 检测指标 / marker (如 MARKER_A, MARKER_PANEL_A)
        assay_type: 实验类型 / assay type (如 WB, Tube, qPCR, cIF)
        stage_batch: 阶段批次 (如 FB1, PB2)

    Returns:
        标准化的实验文件名，格式为 YYMMDD_PROJECT_TARGET_MARKER_ASSAYTYPE_STAGEBATCH
    """
    # 解析日期
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        date_code = date_obj.strftime("%y%m%d")
    except ValueError:
        print(f"错误：日期格式不正确，应为 YYYY-MM-DD，收到：{date_str}", file=sys.stderr)
        sys.exit(1)

    # 验证输入
    if not all([project, target, marker, assay_type, stage_batch]):
        print("错误：所有字段都必须提供", file=sys.stderr)
        sys.exit(1)

    # 生成文件名
    filename = f"{date_code}_{project}_{target}_{marker}_{assay_type}_{stage_batch}"

    return filename


def main():
    if len(sys.argv) != 7:
        print("用法: python generate_experiment_name.py <date> <project> <target> <marker> <assay_type> <stage_batch>")
        print("示例: python generate_experiment_name.py 2026-05-07 PRJ SAMPLE_A MARKER_PANEL_A cIF FB2")
        sys.exit(1)

    date_str = sys.argv[1]
    project = sys.argv[2]
    target = sys.argv[3]
    marker = sys.argv[4]
    assay_type = sys.argv[5]
    stage_batch = sys.argv[6]

    filename = generate_experiment_name(date_str, project, target, marker, assay_type, stage_batch)
    print(filename)


if __name__ == "__main__":
    main()
