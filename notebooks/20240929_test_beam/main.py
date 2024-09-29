import logging
import os
from dotenv import load_dotenv
load_dotenv() 

from apache_beam.options.pipeline_options import PipelineOptions, S3Options
from apache_beam import Map
from apache_beam import Pipeline
from apache_beam.io import ReadFromText

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)

    options = S3Options([
        f"--s3_access_key_id={os.environ['ACCESS_KEY']}",
        f"--s3_secret_access_key={os.environ['SECRET_ACCESS_KEY']}",
        f"--s3_region_name={os.environ['REGION_NAME']}"
    ])

    with Pipeline(options=options) as pipeline:
        data = (
            pipeline
            | "Read from S3" >> ReadFromText("s3://flosbucket/data.txt")
            | "Print elements" >> Map(print)
        )

