import click
import boto3

def add(x,y):
    return x+y

@click.command()
def buckets():
    """This lists my AWS S3 buckets"""

    s3 = boto3.client("s3")
    all_buckets = s3.list_buckets()
    for bucket in all_buckets['Buckets']:
        click.echo(
            click.style(f"bucket: {bucket['Name']}", bg="yellow", fg="blue")
        )


if __name__ == "__main__":
    buckets()