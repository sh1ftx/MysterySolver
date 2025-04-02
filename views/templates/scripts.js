document.addEventListener('DOMContentLoaded', () => {
    const output = document.getElementById('output');
    const input = document.getElementById('input');
  
    // Mensagens iniciais
    const messages = [
      "Welcome, Detective. Type 'start' to begin your investigation.",
      "You can type commands like 'examine', 'interrogate', or 'help'."
    ];
  
    // Exibe as mensagens iniciais no terminal
    messages.forEach(msg => appendMessage(msg));
  
    // Adiciona evento para capturar o comando do usuário
    input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        const command = input.value.trim();
        if (command) {
          appendMessage(`> ${command}`); // Mostra o comando digitado
          handleCommand(command); // Processa o comando
          input.value = ''; // Limpa o campo de entrada
        }
      }
    });
  
    // Função para adicionar mensagens ao terminal
    function appendMessage(message) {
      const messageElement = document.createElement('div');
      messageElement.textContent = message;
      output.appendChild(messageElement);
      output.scrollTop = output.scrollHeight; // Auto-scroll para o final
    }
  
    // Função para processar os comandos do usuário
    function handleCommand(command) {
      if (command === 'start') {
        appendMessage("The case begins. You are at the crime scene.");
      } else if (command === 'help') {
        appendMessage("Available commands: start, examine, interrogate, help.");
      } else if (command === 'examine') {
        appendMessage("You found a mysterious object. Type 'interrogate' to question suspects.");
      } else if (command === 'interrogate') {
        appendMessage("Suspect: 'I was at home during the incident.'");
      } else {
        appendMessage(`Unknown command: ${command}`);
      }
    }
  });