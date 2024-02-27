from kfp.dsl import component


@component
def read_data_op() -> list:
    data = [1, 2, 3, 4]
    return data


@component
def compute_average_op(data: list) -> float:
    return sum(data) / len(data)


@component
def save_result_op(value: float, filename: str = 'result.txt'):
    with open(filename, "w") as f:
        f.write(str(value))
