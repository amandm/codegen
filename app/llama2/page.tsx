"use client";

import { useChat } from "ai/react";
import { useState } from "react"; // Import useState for managing local component state

export default function Chat() {
  const { messages, input, handleInputChange, handleSubmit } = useChat({
    api: "/api/llama2",
  });

  // State for the new text box
  const [newTextBoxValue, setNewTextBoxValue] = useState("");

  // Function to handle button click
  const handleButtonClick = () => {
    setNewTextBoxValue("awwwww"); // Set the new text box value to "awwwww"
  };

  return (
    <div className="space-y-4 max-w-5xl w-full">
      {messages.map((message) => (
        <div
          key={message.id}
          className="whitespace-pre-wrap border border-gray-300 rounded p-2 mb-4"
          style={{ color: message.role === "user" ? "black" : "green" }}
        >
          <strong>{`${message.role}: `}</strong>
          {message.content}
        </div>
      ))}

      <form onSubmit={handleSubmit}>
        <input
          className="w-full max-w-md p-2 border border-gray-300 rounded shadow-xl"
          style={{ marginBottom: "1rem" }}
          value={input}
          placeholder="Say something..."
          onChange={handleInputChange}
        />
        {/* New text box and button */}
        <div>
          <input
            className="w-full max-w-md p-2 border border-gray-300 rounded shadow-xl"
            style={{ marginBottom: "1rem" }}
            value={newTextBoxValue}
            placeholder="This will say awwwww..."
            readOnly // Make this input read-only since its value is controlled by the button
          />
          <button
            type="button" // Ensure this button doesn't submit the form
            className="p-2 bg-blue-500 text-white rounded"
            onClick={handleButtonClick}
          >
            Press me!
          </button>
        </div>
      </form>
    </div>
  );
}
