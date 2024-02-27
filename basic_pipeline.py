from kfp import dsl, compiler
from basic_components import *


@dsl.pipeline(name="My first pipeline", description="A simple pipelines that computes average of array")
def my_pipeline():
    read_data_task = read_data_op()
    compute_average_task = compute_average_op(data=read_data_task.output)
    save_result_task = save_result_op(value=compute_average_task.output)


compiler.Compiler().compile(my_pipeline, 'my_pipeline.json')
