from flask import Flask,jsonify,render_template,request,redirect

from db import *


app=Flask(__name__)

#configuring mongodb
app.config['MONGODB_HOST']=url
mydb.init_app(app)

@app.route("/shortlist",methods=['GET','POST'])
def performFilter():
    if request.method=="GET":
        return render_template("filter.html")
    else:
        mod=request.form['bikemodel']
        tp=request.form['type']
        reg=request.form['regno']
        cost=request.form['price']
        
        if mod!="" and tp=="Select type" and reg=="" and cost=="":
            collected=Details.objects(bikemodel__startswith=mod)
            return render_template("view.html",data=collected)
        elif mod=="" and tp!="Select type" and reg=="" and cost=="":
            collected=Details.objects(type__iexact=tp)
            return render_template("view.html",data=collected)
        # elif mod=="" and tp=="Select type" and reg!="" and cost=="":
        #     reg=(reg)
        #     collected=Details.objects(reg__gte=reg)
        #     return render_template("view.html",data=collected)
        elif mod=="" and tp=="Select type" and reg=="" and cost!="":
            cost=int(cost)
            collected=Details.objects(price__lte=cost)
            return render_template("view.html",data=collected)
        else:
            return render_template("filter.html")


@app.route("/erase/<mod>")
def performDelete(mod):
    collected=Details.objects(bikemodel=mod).first()
    collected.delete()
    return redirect("/list")

@app.route("/update/<mod>",methods=["GET","POST"])
def performEdit(mod):
    if request.method=="GET":
        collected=Details.objects(bikemodel=mod).first()
        return render_template("edit.html",data=collected)
    else:
        bikemodel=request.form['bikemodel']
        bikename=request.form['bikename']
        regno=request.form['regno']
        cc=int(request.form['cc'])
        price=int(request.form['price'])
        stock=int(request.form['stock'])
        type=request.form['type']
        
        Details.objects(bikemodel=bikemodel).update_one(set__bikename=bikename,set__regno=regno,
                                               set__cc=cc,set__price=price,set__stock=stock,
                                               set__type=type)
        return redirect("/list")




@app.route("/pick/<mod>")
def showRead(mod):
    collected=Details.objects(bikemodel=mod).first()
    return render_template("read.html",data=collected)

@app.route("/new",methods=['GET','POST'])
def newOne():
    if request.method=="GET":
        return render_template("newbike.html")
    else:
        details=Details()
        details.bikemodel=request.form['bikemodel']
        details.bikename=request.form['bikename']
        details.regno=request.form['regno']
        details.cc=int(request.form['cc'])
        details.price=int(request.form['price'])
        details.stock=int(request.form['stock'])
        details.type=request.form['type']
        
        details.save()
        
        return redirect("/list")

@app.route("/")
def showHome():
    return render_template("navigation.html")

@app.route("/list")
def listAll():
    collected=Details.objects.all()
    return render_template("view.html",data=collected)

@app.route("/test")
def checkconnectio():
    return jsonify(Details.objects.all())


if __name__=="__main__":
    app.run(debug=True,port=1127)
