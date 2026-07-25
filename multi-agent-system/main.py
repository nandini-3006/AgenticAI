from graph import app

query=input("Ask: ")

result=app.invoke(

{

"user_query":query

}

)

print(result["answer"][0]["text"])