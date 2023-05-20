import json
from django.views.generic.base import TemplateView
import os
from langchain import SQLDatabaseChain, PromptTemplate, OpenAI
from langchain.sql_database import SQLDatabase
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from langchain.chat_models import ChatOpenAI

os.environ['OPENAI_API_KEY'] = "use your open api key here"


@method_decorator(csrf_exempt, name='dispatch')
class ChatWithData(TemplateView):
    def get(self, request, *args, **kwargs):
        search_query = request.GET.get('query')
        print("search query is ", search_query)
        db = SQLDatabase.from_uri("mysql+pymysql://root:password@localhost/student")
        _DEFAULT_TEMPLATE = """Given an input question, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
        Use the following format:

        Question: "Question here"
        SQLQuery: "SQL Query to run"
        SQLResult: "Result of the SQLQuery"
        Answer: "Final answer here"

        Only use the following tables:

        {table_info}

        If someone asks for the table foobar, they really mean the employee table.

        Question: {input}"""
        PROMPT = PromptTemplate(
            input_variables=["input", "table_info", "dialect"], template=_DEFAULT_TEMPLATE
        )

        llm = ChatOpenAI(model_name="gpt-3.5-turbo")
        # llm = OpenAI(temperature=0)
        # gpt - 3.5 - turbo - 0301
        db_chain = SQLDatabaseChain(llm=llm, database=db, prompt=PROMPT, verbose=True, return_intermediate_steps=True)
        result = db_chain(search_query)
        converted_result = json.dumps(result)
        ans = json.loads(converted_result)
        data = {
            'message': ans["result"]
        }
        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class Dashboard(TemplateView):
    template_name = "admin/dashboard.html"
