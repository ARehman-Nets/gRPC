---

# 🐍 Simple gRPC Python Example

A minimal Python project demonstrating how to build a gRPC server and client using Protocol Buffers.

---

## 📌 Overview

This example walks through:

- Defining a gRPC service in a `.proto` file  
- Generating Python code using `grpcio-tools`  
- Implementing a basic greeting server  
- Creating a client that calls the server  

---

## ✨ Features

- ✅ Protocol Buffers-based service definition  
- ✅ Unary RPC method: `SayHello`  
- ✅ Python gRPC server using `grpcio`  
- ✅ Python client using generated stubs  
- ✅ Easily extensible to streaming or advanced RPCs  

---

## 🧰 Technologies

| Tool              | Purpose                                 |
|-------------------|------------------------------------------|
| gRPC              | Remote procedure call framework          |
| Protocol Buffers  | Efficient data serialization             |
| grpcio            | Python gRPC runtime                      |
| grpcio-tools      | Python code generation from `.proto`     |

---

## ⚙️ Setup & Installation

1. **Create `requirements.txt`**  
   ```
   grpcio
   grpcio-tools
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate Python code from `.proto`**  
   ```bash
   python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. greeting.proto
   ```

---

## 🚀 Running the Project

### Start the Server  
```bash
python server.py
```
> Server listens on port `50051`.

### Run the Client  
```bash
python client.py
```

**Expected Output:**  
```
Greeting from server: Hello, Alice!
```

---

## 📁 File Structure

```
├── greeting.proto               # Service & message definitions
├── greeting_pb2.py              # Generated protobuf classes
├── greeting_pb2_grpc.py         # Generated gRPC classes
├── server.py                    # gRPC server implementation
├── client.py                    # gRPC client implementation
├── requirements.txt             # Python dependencies
```

---

## 🔍 How It Works

1. Define service and messages in `greeting.proto`  
2. Generate Python bindings using `grpc_tools.protoc`  
3. Implement server logic in a service class  
4. Use client stub to call server methods like local functions  
5. gRPC handles networking, serialization, and method dispatch  

---

## 🛠️ Next Steps

- Add streaming RPCs (client, server, bidirectional)  
- Implement authentication and error handling  
- Secure the server with TLS encryption  

---

## 👤 Author

**Abdul Rehman**  
Feel free to reach out if you have questions or want to extend this project! 😊

---

Would you like me to turn this into a GitHub README or a LinkedIn post next?
