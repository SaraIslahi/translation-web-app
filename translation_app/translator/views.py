from django.shortcuts import render
from django.conf import settings
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
import uuid

def translate_view(request):
    context = {}

    if request.method == "POST":
        text = request.POST.get("text", "").strip()
        target = request.POST.get("target", "fr")
        tts_choice = request.POST.get("tts", "yes")

        context["text"] = text
        context["target"] = target
        context["tts"] = tts_choice

        if not text:
            context["error"] = "Please enter some text."
            return render(request, "translator/translate.html", context)

        try:
            # ✅ auto-detect source language
            translated = GoogleTranslator(source="auto", target=target).translate(text)
            context["translated"] = translated

            # ✅ generate audio if requested
            if tts_choice == "yes":
                media_dir = os.path.join(settings.BASE_DIR, "media")
                os.makedirs(media_dir, exist_ok=True)

                filename = f"tts_{uuid.uuid4().hex}.mp3"
                file_path = os.path.join(media_dir, filename)

                # gTTS language must be supported; use target language
                tts = gTTS(text=translated, lang=target)
                tts.save(file_path)

                context["audio_url"] = f"/media/{filename}"

        except Exception as e:
            context["error"] = f"Error: {e}"

    return render(request, "translator/translation.html", context)
