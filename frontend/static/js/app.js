document.addEventListener("DOMContentLoaded", () => {
  fetch("/api/health")
    .then(response => response.json())
    .then(data => {
      document.getElementById("status").innerText =
        `Backend: ${data.status} | Database: ${data.database}`;
      document.getElementById("status").className = "success";
    })
    .catch(error => {
      console.error(error);
      document.getElementById("status").innerText =
        "Backend not reachable";
      document.getElementById("status").className = "error";
    });
});
