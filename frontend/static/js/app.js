function checkHealth() {
   fetch("http://localhost:5000/health")

        .then(response => response.json())
        .then(data => {
            document.getElementById("result").innerText =
                "Backend Status: " + data.status;
        })
        .catch(error => {
            document.getElementById("result").innerText =
                "Backend is not reachable";
        });
}
