import boto3
from flask import Flask, jsonify, request

session = boto3.Session(profile_name="ta-landing")
s3 = session.client("s3")
# Let's use Amazon S3
# Print out bucket names
app = Flask(__name__)
response = s3.list_buckets()
print("Existing buckets:")
for bucket in response["Buckets"]:
    print(f'  {bucket["Name"]}')


@app.route("/", methods=["GET"])
def list_files():
    # Get the bucket name and folder name from the request arguments
    # bucket_name = request.args.get("bucket")
    bucket_name = "tiger-mle-pg"
    # folder_name = request.args.get("folder")
    folder_name = "home/sai.paleti"

    if not bucket_name or not folder_name:
        return jsonify({"error": "Bucket name and folder name are required"}), 400

    try:
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)

        if "Contents" in response:
            files = [obj["Key"] for obj in response["Contents"]]
        else:
            files = []

        files_list_html = "<ul>"
        for file in files:
            files_list_html += f"<li>{file}</li>"
        files_list_html += "</ul>"
        return files_list_html
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=8085)
