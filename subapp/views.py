from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def match(request):
    # print(request.method)
    if request.method =='POST':
        name1s=request.POST['n1']
        name2s=request.POST['n2']
        name1a=name1s
        name2a=name2s
        # print(name1s,name2s)
        name1s.lower()
        name2s.lower()
        name1=[]
        for i in name1s:
            if i.isalpha():
                name1.append(i)
        name2=[]
        for i in name2s:
            if i.isalpha():
                name2.append(i)
        for i in range(0,len(name1)):
            if name1[i] != '*':
                for j in range(0,len(name2)):
                    if name2[j] != '*':
                        if name1[i] == name2[j]:
                            name1[i]='*'
                            name2[j]='*'
                            break
        count=0
        for i in name1:
            if i != '*':
                count+=1
        for i in name2:
            if i != '*':
                count+=1
        checker=['F','L','A','M','E','S']
        ind=0
        for i in range(6,1,-1):
            if ind==len(checker):
                ind-=1
            num=count%i
            if num==0:
                j=1
                while(j<i):
                    if ind==len(checker)-1:
                        ind=0
                        j+=1
                    else:
                        ind+=1
                        j+=1
                checker.remove(checker[ind])
                if ind==len(checker):
                    ind=0
            else:
                l=0
                while(l<num):
                    if l==0:
                        ind=ind
                    else:
                        if ind==len(checker)-1:
                            ind=0
                        else:
                            ind+=1
                    l+=1
                checker.remove(checker[ind])
                if ind==len(checker):
                    ind=0
        # print(checker)
        full1={
            'F':f'You({name1a}) 👯 are the Friend of {name2a}',
            'L':f'{name2a} Lo❤️e {name1a}',
            'A':f'You({name1a}) have 🧲 Attraction on {name2a}',
            'M':f':You({name1a})  going to 💑🏼 Marry {name2a}',
            'E':f'{name2a} is 👾 Enemy',
            'S':f'{name2a} is 👧👧 Sibling for you({name1a})'
        }
        full2={
            'F':'👯',
            'L':'❤️',
            'A':'🧲',
            'M':'💑🏼',
            'E':'👾',
            'S':'👧👧'
        }
        val=checker[0]
        # val='S'
        out=full1[val]
        emj=full2[val]
        # print(out)
        return render(request,'match.html',{'ma':out,'emj':emj})
    return render(request,'home.html')