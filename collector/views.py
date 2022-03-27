from django.shortcuts import render
from . import forms
from . import models


def dashboard(request):
    return render(request, 'collector/recorder.html', {})
    # if request.user.is_authenticated():
    #     try:
    #         user_prompts = models.audio_files.objects.filter(user=request.user)
    #         last_prompt = user_prompts[-1]
    #         if last_prompt.id < models.sentences.TOTAL_PROMPTS:
    #             new_prompt_id = last_prompt.id + 1
    #             new_prompt = models.sentences.objects.get(id=new_prompt_id)
    #         context = {'prompt': new_prompt.sentence,
    #                    'id': new_prompt.id}
    #     except BaseException as e:
    #         first_prompt = models.sentences.objects.get(id=0)
    #         context = {'prompt': first_prompt.sentence,
    #                    'id': first_prompt.id}
    #     return render(request, 'collector/recorder.html', context)
    # else:
    #     return HttpResponseRedirect('/')


def upload_audio(request):
    if request.method == 'POST':
        audio_upload = forms.audio_upload_form(request.POST, request.FILES)
        if audio_upload.is_valid():
            audio = audio_upload.save(commit=False)
            prompt = models.sentence.get(id=request.POST['pid'])
            audio.sentence = prompt
            audio.user = request.user
            audio.audio.name = str(audio.user.id) + "_" + str(audio.sentence.id) + ".wav"
            audio.save()
        else:
            context = {"errors": audio_upload.errors}
    return HttpResponseRedirect('/user/dashboard')
