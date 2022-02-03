import json
import os
import requests
if os.path.exists("course.json"):
    pass
else:
    file=open("course","w")
    file.close()
def request():
    req=requests.get("http://saral.navgurukul.org/api/courses")
    # print(req)
    with open("course.json","w")as file:
       dic=json.loads(req.text) 
       json.dump(dic,file,indent=4)
    with open("course.json","r")as read1:
        read2=json.load(read1)
        print(read2)
        n=1
        id=[]
        for i in read2["availableCourses"]:
            print(n,i["name"],":-",i["id"])
            id.append(i["id"])
            n=n+1
        course_id=int(input("enter number:"))
        req2=requests.get("http://saral.navgurukul.org/api/courses/"+str(id[course_id-1])+"/exercises")
        course_detail=req2.json()
        detail_count=1
        slug=[]
        for name in course_detail["data"]:
            print(detail_count,":-",name["name"])
            slug.append(name["slug"])
            detail_count=detail_count+1
        slug_input=int(input("enter number"))
        slug_api=requests.get("http://saral.navgurukul.org/api/courses/"+str(course_id)+"/exercise/getBySlug?slug="+slug[slug_input])
        slug_json=slug_api.json()
        print(slug_json["content"])
        print("up':-for previous content")
        print("next':- for previous content")
        print("same':-for previous content")
        for s in range(4):
            step=input("enter:")
            # while step<=3:
            if step=="next":
                slug_api=requests.get("http://saral.navgurukul.org/api/courses/"+str(course_id)+"/exercise/getBySlug?slug="+slug[slug_input+1]      )
                up_json=slug_api.json()
                print(slug_input+1,up_json["content"])
            elif step=="up":
                slug_api=requests.get("http://saral.navgurukul.org/api/courses/"+str(course_id)+"/exercise/getBySlug?slug="+slug[slug_input-1])
                next_json=slug_api.json()
                print(slug_input-1,next_json["content"])
            elif step=="same":
                slug_api=requests.get("http://saral.navgurukul.org/api/courses/"+str(course_id)+"/exercise/getBySlug?slug"+slug[slug_input])
                same_json=slug_api.json()
                print(slug_input,same_json["content"])
            elif step=="exit":
                request()
request()