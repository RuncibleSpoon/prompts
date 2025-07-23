import os
import tempfile

def process_uploaded_file(file_stream, filename, max_size=10*1024*1024):
    # Validate filename: allow only safe characters
    safe_filename = os.path.basename(filename)
    if safe_filename != filename:
        raise ValueError("Invalid filename.")

    # Limit file size
    file_stream.seek(0, os.SEEK_END)
    size = file_stream.tell()
    if size > max_size:
        raise ValueError("File too large.")
    file_stream.seek(0)

    # Save to a secure temporary directory
    with tempfile.NamedTemporaryFile(delete=True, prefix="upload_", suffix=os.path.splitext(safe_filename)[1]) as tmp:
        tmp.write(file_stream.read())
        tmp.flush()
        tmp.seek(0)
        # Process the file as needed, e.g., read contents
        data = tmp.read()
        # ... process data securely ...

    return "File processed successfully."

# Example usage (simulate file upload):
if __name__ == "__main__":
    import io
    # Simulate a file upload with a BytesIO object
    fake_file = io.BytesIO(b"example content")
    try:
        result = process_uploaded_file(fake_file, "user_data.txt")
        print(result)
    except Exception as e:
        print(f"Error: {e}")