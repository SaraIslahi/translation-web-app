from django.shortcuts import render
from django.conf import settings
from pathlib import Path
import uuid

# Option A: googletrans (easy demo)  -> pip install googletrans==4.0.0-rc1
from googletrans import Translator

# Option A for audio: gTTS -> pip install gTTS
from gtts import gTTS


translator = Translator()


def translate_view(request):
    context = {
        "text": "",
        "target": "fr",
        "tts": "yes",
        "translated": "",
        "audio_url": "",
        "error": "",
    }

    if request.method == "POST":
        text = (request.POST.get("text") or "").strip()
        target = request.POST.get("target") or "fr"
        tts = request.POST.get("tts") or "yes"

        context["text"] = text
        context["target"] = target
        context["tts"] = tts

        if not text:
            context["error"] = "Please enter some text to translate."
            return render(request, "translate.html", context)

        try:
            # Translate
            result = translator.translate(text, dest=target)
            translated_text = result.text
            context["translated"] = translated_text

            # Optional audio generation
            if tts == "yes":
                audio_dir = Path(settings.MEDIA_ROOT) / "audio"
                audio_dir.mkdir(parents=True, exist_ok=True)

                filename = f"tts_{uuid.uuid4().hex}.mp3"
                filepath = audio_dir / filename

                # gTTS needs a supported language code
                tts_obj = gTTS(text=translated_text, lang=target)
                tts_obj.save(str(filepath))

                context["audio_url"] = f"{settings.MEDIA_URL}audio/{filename}"

        except Exception as e:
            context["error"] = f"Translation failed: {e}"

    return render(request, "translator/translation.html", context)

index = translate_view
