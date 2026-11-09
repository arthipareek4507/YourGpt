const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendButton = document.getElementById("send-button");

// Display a message in the chat window
function addMessage(message, sender) {
    const messageDiv = document.createElement("div");

    messageDiv.classList.add(sender + "-message");
    messageDiv.textContent = message;

    chatBox.appendChild(messageDiv);

    // Automatically scroll to the latest message
    chatBox.scrollTop = chatBox.scrollHeight;
}

function showTypingIndicator() {
    const typingDiv = document.createElement("div");

    typingDiv.classList.add("bot-message", "typing-indicator");
    typingDiv.textContent = "...";

    chatBox.appendChild(typingDiv);
    chatBox.scrollTop = chatBox.scrollHeight;

    return typingDiv;
}

// Handle sending a message
async function sendMessage() {
    const message = userInput.value.trim();

    if (message === "") {
        return;
    }

    addMessage(message, "user");

    userInput.value = "";
    userInput.disabled = true;
    sendButton.disabled = true;

    const typingDiv = showTypingIndicator();

    try {
        const response = await fetch("/chat", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        if (!response.ok) {
           throw new Error(data.response || "Something went wrong");
        }

        typingDiv.remove();

        addMessage(data.response, "bot");

    } catch (error) {
        typingDiv.remove();
        addMessage("Oops! Something went wrong. Please try again.", "bot");

        console.error("Error:", error);

    } finally {
        userInput.disabled = false;
        sendButton.disabled = false;
        userInput.focus();
    }
}
// Send message when button is clicked
sendButton.addEventListener("click", sendMessage);

// Send message when Enter is pressed
userInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});