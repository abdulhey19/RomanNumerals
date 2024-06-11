romanNumerals={
    'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
}

def romanConvertToInteger(sayi):
    result = 0
    cnt=0
    try:
        for s in range(len(sayi)-1):

             nums1=romanNumerals.get(sayi[s])
             nums2=romanNumerals.get(sayi[s+1])

             if not isinstance(nums1, int) or not isinstance(nums2, int):

                 # nums1 ve nums2 nin de none gelip gelmediğini kontrol ediyor...
                 raise TypeError()

             if s < len(sayi)-3 and sayi.rfind(sayi[s]*4) != -1:

                 # herhangi bir rakam üste üste 4 kez tekrar edip etmediğini kontrol eden blok
                 raise ValueError()

             if s < len(sayi)-2 and not romanNumerals.get(sayi[s]) >= romanNumerals.get(sayi[s+2]):
                 print("3")
                 raise ValueError()

             if nums1 >= nums2:
                 #burada kontrol ile sayının önündeki sayıdan büyük olması toplama yap demek...
                 result += nums1
             else:
                 if nums2/nums1 == 10 or nums2/nums1 == 5:
                     result -= nums1
                 else:
                     raise ValueError()
        result += romanNumerals.get(sayi[len(sayi) - 1])
    except TypeError:
        result = "Böyle bir romen rakamı yok..."
    except ValueError:
        result = "Romen rakamlarının dizilimi yanlış..."

    return result


