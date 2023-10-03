from flask import Flask  # Ensure you have correct casing here

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"
'''
<html>
<body>
<center>
<h1>Demo on GitOps with ArgoCD and Github Actions.</h1> <br>
<br>
<img src="https://github.com/solarge/cicd-eks-gha/blob/main/itsworking.jpeg?raw=true">
</center>
</body>
</html>
'''
