import os

def modify_imports(directory, package_name):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith("_pb2.py") or file.endswith("_pb2_grpc.py"):
                file_path = os.path.join(root, file)
                print(f"Modifying imports in: {file_path}")
                with open(file_path, 'r') as f:
                    content = f.readlines()

                with open(file_path, 'w') as f:
                    for line in content:
                        if line.startswith("from ") and f"v1" in line:
                            line = line.replace("from ", f"from {package_name}.")
                        f.write(line)

if __name__ == "__main__":
    modify_imports('gen/python', 'protos')
