from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.session import *
from pywebio.pin import *
import openai


def Oscar():
    put_html("<center><h2>بايثون والذكاء الاصطناعي تقنيةchatGpt  </h2></center>") .style("color:tomato; padding:1px;")
    put_html("<center><img src ='https://academy.hsoub.com/uploads/monthly_2023_01/12761316_--.png.3460d23fe4d47de9e1a3799b0918c57c.png'width='400'></center>")
    openai.api_key ="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"
    ask = input('oscar : ماذا تريد ان تبرمج ؟')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=ask,
        temperature=0.9,
        max_tokens=1200,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    text = response['choices'][0]['text']
    code = textarea('code edit : [نتيجة البحث الخاصه بك ]',
      code={
      'mode' : "python",
      'theme' : 'dracula',
  }, value=text)

start_server (Oscar ,port=1985, debug=True)
#localhost:1985
