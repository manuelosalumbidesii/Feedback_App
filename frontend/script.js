document.getElementById("feedback-form").addEventListener("submit", async function (e) {
  e.preventDefault();

  const name = document.getElementById("name").value;
  const message = document.getElementById("message").value;

  try {
    const response = await fetch("/api/feedback", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name, message }),
    });

    const data = await response.json();
    document.getElementById("response-msg").innerText = data.message;
  } catch (error) {
    console.error("Error submitting feedback:", error);
    document.getElementById("response-msg").innerText = "Something went wrong.";
  }
});
