import boto3
import os

def main():
    # Получаем учетные данные из переменных окружения
    access_key = os.getenv('AWS_ACCESS_KEY_ID')
    secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    endpoint_url = os.getenv('S3_ENDPOINT_URL')
    bucket_name = os.getenv('BUCKET_NAME')

    # Создаем сессию
    session = boto3.session.Session()
    s3_client = session.client(
        service_name='s3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        endpoint_url=endpoint_url
    )

    # Проверяем доступ к бакету
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        print(f"Contents of bucket {bucket_name}:")
        for obj in response.get('Contents', []):
            print(obj['Key'])
    except Exception as e:
        print(f"Error accessing bucket {bucket_name}: {e}")

if __name__ == "__main__":
    main()
