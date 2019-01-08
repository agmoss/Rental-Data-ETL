class Rental:

    def __init__(self,ref_id,userId , _id ,title ,price,_type ,sq_feet,availability,avdate,
            location ,rented ,thumb , thumb2 ,slide , link ,latitude , longitude,marker ,address, address_hidden,  
            city ,province , intro , community ,quadrant , phone , phone_2 ,preferred_contact ,website, email ,  
            status , bedrooms = 0 , den = " " ,baths = " " ,  cats = " " , dogs = " " ,utilities_included = " ", retrieval_date = " "):
            
                self.ref_id = ref_id
                self.id = _id
                self.userId = userId
                self.title = title
                self.price = price
                self.type = _type
                self.sq_feet = sq_feet
                self.availability = availability
                self.avdate = avdate
                self.location = location
                self.rented = rented
                self.thumb = thumb
                self.thumb2 = thumb2
                self.slide = slide
                self.link = link
                self.latitude = latitude
                self.longitude = longitude
                self.marker = marker
                self.address = address
                self.address_hidden = address_hidden
                self.city = city
                self.province  = province
                self.intro = intro
                self.community = community
                self.quadrant = quadrant
                self.phone = phone
                self.phone_2 = phone_2
                self.preferred_contact = preferred_contact
                self.website = website
                self.email = email
                self.status = status
                self.bedrooms = bedrooms
                self.den = den
                self.baths = baths
                self.cats = cats               
                self.dogs = dogs
                self.utilities_included = utilities_included             
                self.retrieval_date = retrieval_date            