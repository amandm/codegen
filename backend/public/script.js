document.getElementById('codeForm').onsubmit = async function(e) {
    e.preventDefault();
    const description = document.getElementById('description').value;
    const response = await fetch('/generate-code/', {
        method: 'POST',
        headers: {
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"

        },
        body: {description: description},
    });
    if (response.ok) {
        const data = await response.json();
        document.getElementById('generatedCode').textContent = data.generated_code;
    } else {
        alert('Failed to generate code. Please try again.');
    }
}
