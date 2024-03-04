import com.sun.speech.freetts.Voice;
import com.sun.speech.freetts.VoiceManager;
/**
 * Beschreiben Sie hier die Klasse Voice.
 * 
 * @author Dawid Szymon Kazek     
 * @version 0.1
 */


public class TextToSpeech {
    private static final String VOICE_NAME = "kevin16";

    public static void speak(String text) {
        Voice voice;
        VoiceManager voiceManager = VoiceManager.getInstance();
        voice = voiceManager.getVoice(VOICE_NAME);
        voice.allocate();
        voice.speak(text);
        voice.deallocate();
    }

    public static void main(String[] args) {
        speak("Hello, I can speak now");
    }
}
