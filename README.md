# ExiPet - Pet Adoption 

#### This is my Django project, built using Django Rest Framework (DRF). The project is a Pet Adoption Platform that provides users with various features to explore, adopt, and manage pet listings. Key functionalities included: 
---
## Admin

- Admin can log in and log out.
- Admin can manage the dashboard.
- Admin can manage profile.
- Admin can add, edit, and delete any post.

## User

- Users can register, log in, and log out.
- User can add post.
- User can only edit and delete their post.
- Users can adopt pets.
- User can review the pet he/she adopted.
- User can filter pets category-wise.

## Features

### Authentication

- New users can register on the platform using their email. An activation link is sent to their email to verify and activate their account, ensuring a secure onboarding process.

### Pet Adoption

- Users can browse available pets for adoption, view detailed pet information, and adopt pets through a simple and intuitive process.

### Pet Filtering

- Users can easily filter pets by category to smooth their search for specific pets.

### User Generated Content

- Users can add pets for others to adopt, with the ability to edit or delete their posts at any time.

### Review system

- After successfully adopting a pet, users can leave reviews, and review options are visible in their profile.

### Profile Management

- Each user has a personal profile page where they can:

     ⚡ View their account information and balance 
      
     ⚡ See the available posts that they have listed but that hasn't been adopted yet.
      
     ⚡ View their adoption history.

### Adoption History

- A dedicated section that displays the user's adoption history, providing a clear overview of their activity on the platform.

### Admin Controls

- Administrators have full access to manage the platform. They can add, edit, and delete posts, ensuring the site's smooth operation and integrity.
  
### Admin Dashboard

- Admin can see important information here, add post and see models as table view.


## API Endpoints

- ### Customer

      POST /customer/register
      POST /customer/login
      POST /customer/logout
      POST /customer/pass_change
      POST /customer/create_review
      PUT /customer/update_profile

- ### Pet

      POST /pet/list
      POST /pet/type
      POST /pet/adoption
      POST /pet/post
      PUT /pet/post/<int:pk>
      Delete /pet/post/<int:pk>
  
- ### Others

      POST /service
      POST /contact_us
      POST /member
      POST /member
      PUT /transaction/deposit
      PUT /transaction/withdraw


## 💻 Technology: 

- Django
- Django Rest Framework (DRF)
- PostgreSQL
- etc.

---

## 🌐 Deployment: API Deployed using Vercel.
Front-end Live: https://exipet.netlify.app/

## 🌐 Deployment: API Deployed using Vercel.
API Live link: https://exi-pet-drf.vercel.app/

## GitHub!
Frontend: https://github.com/asirff399/ExiPet