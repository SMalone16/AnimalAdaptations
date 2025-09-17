function setupSpeechButtons() {
  const buttons = document.querySelectorAll('.speak-button');
  buttons.forEach((button) => {
    button.addEventListener('click', () => {
      const text = button.getAttribute('data-speech');
      if (!text) return;

      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = 'en-US';
      utterance.rate = 1;
      window.speechSynthesis.speak(utterance);
    });
  });
}

document.addEventListener('DOMContentLoaded', () => {
  setupSpeechButtons();
});
