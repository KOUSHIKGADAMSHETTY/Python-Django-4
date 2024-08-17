from django.shortcuts import render

students ={'info': [
    {'name': 'ram', 'semester': 6 , 'cgpa': 9.1, 'department': 'Computer science engineering'},
    {'name': 'vaali', 'semester': 6 , 'cgpa': 8.1, 'department': 'Mechanical engineering'},
    {'name': 'sugriva', 'semester': 6 , 'cgpa': 8.6, 'department': 'Civil engineering'}
]}

def find(request,name):
    result = None
    for record in students.get('info'):
        if record.get('name')==name:
            result=record
            break
    if result is not None:     
        return render(request, 'newdata.html',{'student':result})
    else:
        return render(request,'newdata.html',{'student':None})


