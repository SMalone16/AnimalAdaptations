const ME_SPEAK_SCRIPT = 'https://cdn.jsdelivr.net/npm/mespeak/mespeak.min.js';
const ME_SPEAK_CONFIG = 'https://cdn.jsdelivr.net/npm/mespeak/mespeak_config.json';
const ME_SPEAK_VOICE = 'https://cdn.jsdelivr.net/npm/mespeak/voices/en/en.json';

let meSpeakInitPromise = null;

function ensureMeSpeakReady() {
  if (
    window.meSpeak &&
    typeof window.meSpeak.isConfigLoaded === 'function' &&
    window.meSpeak.isConfigLoaded() &&
    typeof window.meSpeak.isVoiceLoaded === 'function' &&
    window.meSpeak.isVoiceLoaded('en/en')
  ) {
    return Promise.resolve(true);
  }

  if (meSpeakInitPromise) {
    return meSpeakInitPromise;
  }

  meSpeakInitPromise = new Promise((resolve) => {
    const script = document.createElement('script');
    script.src = ME_SPEAK_SCRIPT;
    script.async = true;

    script.onload = () => {
      if (!window.meSpeak) {
        meSpeakInitPromise = null;
        resolve(false);
        return;
      }

      Promise.all([
        fetch(ME_SPEAK_CONFIG).then((response) => {
          if (!response.ok) {
            throw new Error('Failed to load meSpeak config');
          }
          return response.json();
        }),
        fetch(ME_SPEAK_VOICE).then((response) => {
          if (!response.ok) {
            throw new Error('Failed to load meSpeak voice');
          }
          return response.json();
        }),
      ])
        .then(([config, voice]) => {
          window.meSpeak.loadConfig(config);
          window.meSpeak.loadVoice(voice);
          resolve(true);
        })
        .catch((error) => {
          console.warn('Unable to initialise meSpeak:', error);
          meSpeakInitPromise = null;
          resolve(false);
        });
    };

    script.onerror = () => {
      console.warn('Unable to load meSpeak script');
      meSpeakInitPromise = null;
      resolve(false);
    };

    document.head.appendChild(script);
  });

  return meSpeakInitPromise;
}

function speakWithMeSpeak(text) {
  return ensureMeSpeakReady().then((ready) => {
    if (!ready || !window.meSpeak) {
      return false;
    }

    try {
      window.meSpeak.stop();
      window.meSpeak.speak(text, {
        amplitude: 100,
        wordgap: 4,
        pitch: 55,
        speed: 165,
        voice: 'en/en',
      });
      return true;
    } catch (error) {
      console.warn('meSpeak could not play audio:', error);
      return false;
    }
  });
}

function speakWithBrowser(text) {
  if (!('speechSynthesis' in window)) {
    console.warn('Browser speech synthesis is unavailable.');
    return;
  }

  window.speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = 'en-US';
  utterance.rate = 0.95;
  utterance.pitch = 1;
  window.speechSynthesis.speak(utterance);
}

function setButtonBusy(button, busy) {
  button.disabled = busy;
  button.classList.toggle('is-speaking', busy);
  button.setAttribute('aria-busy', busy ? 'true' : 'false');
}

function setupSpeechButtons() {
  const buttons = document.querySelectorAll('.speak-button');
  buttons.forEach((button) => {
    button.addEventListener('click', () => {
      const text = button.getAttribute('data-speech');
      if (!text) {
        return;
      }

      setButtonBusy(button, true);

      speakWithMeSpeak(text)
        .then((played) => {
          if (!played) {
            speakWithBrowser(text);
          }
        })
        .finally(() => {
          setTimeout(() => {
            setButtonBusy(button, false);
          }, 400);
        });
    });
  });
}

document.addEventListener('DOMContentLoaded', () => {
  setupSpeechButtons();
});
