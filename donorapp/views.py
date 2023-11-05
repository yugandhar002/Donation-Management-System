from django.shortcuts import render

from adminapp.models import Donor,Organisation,Admin,Donororgmapping


def donorhome(request):
    dname=request.session['dname']
    don=Donor.objects.get(name=dname)
    return render(request,'donorhome.html',{'dname':dname,"don":don})
def donordonate(request):
    dname=request.session['dname']
    org=Organisation.objects.all()
    return render(request,'donordonate.html',{'dname':dname,'organisation':org})
def donorchangepwd(request):
    dname=request.session['dname']
    return render(request,'donorchangepwd.html',{'dname':dname})
def donorpwdupdated(request):
    dname=request.session['dname']
    opwd=request.POST['opwd']
    npwd=request.POST['npwd']
    flag=Donor.objects.filter(password=opwd,name=dname)
    if flag:
        Donor.objects.filter(name=dname,password=opwd).update(password=npwd)
        message="password update successfully"
        return render(request,'donorchangepwd.html',{'dname':dname,'msg':message})
    else:
        message="enter valid old password"
        return render(request,'donorchangepwd.html',{'dname':dname,'msg':message})
def donormakedonation(request):
    dname=request.session['dname']
    return render(request,"donormakedonation.html",{'dname':dname})
def donordonated(request):
    dname=request.session['dname']
    name=request.POST['oname']
    amt=request.POST['amt']
    donororg=Donororgmapping(donor=Donor.objects.get(name=dname),organisation=Organisation.objects.get(name=name),amount=amt)
    Donororgmapping.save(donororg)
    message="Transaction Successful"
    return render(request,'donormakedonation.html',{'dname':dname,'msg':message})
def donormydonations(request):
    dname=request.session['dname']
    donororg=Donororgmapping.objects.all()
    dor=[]
    for i in donororg:
        if i.donor.name==dname:
            dor.append(i)
    return render(request,'donormydonations.html',{'dname':dname,'dorg':dor})




