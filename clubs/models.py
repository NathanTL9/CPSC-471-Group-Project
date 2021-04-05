from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User



class University(models.Model):
    schoolID = models.CharField(max_length=200, primary_key = True)
    name = models.CharField(max_length=200, default = "none")
    location = models.CharField(max_length=200, default = "none")

    def __str__(self):
        return self.schoolID

class Club(models.Model):
    club_name = models.CharField(max_length=200, primary_key = True)
    schoolID = models.ForeignKey(University, to_field='schoolID', default = "none", on_delete=models.CASCADE)
    club_type = models.CharField(max_length=200, default = "none")
    club_budget = models.IntegerField(default= 0)
    contactEmail = models.EmailField(default = "nullnull@null.ca")


    def __str__(self):
        return self.club_name



class Room(models.Model):
    RoomNo = models.IntegerField(default = 0, primary_key = True)
    schoolID = models.ForeignKey(University, to_field='schoolID', on_delete=models.CASCADE)
    buildingName = models.CharField(max_length=200, default = "none")
    Capacity = models.IntegerField(default= 0)
    location = models.CharField(max_length=200, default = "none")



    def __str__(self):
        return self.RoomNo


class Event(models.Model):
    clubname = models.ForeignKey(Club, to_field='club_name', on_delete=models.CASCADE)
    RoomNo = models.ForeignKey(Room, to_field='RoomNo', on_delete=models.CASCADE)
    date = models.DateTimeField('Event date', default=datetime.now)
    event_type = models.CharField(max_length=200, default = "none")
    description = models.CharField(max_length=200, default = "none")

    def __str__(self):
        return self.event_description



class Announcment(models.Model):
    clubname = models.ForeignKey(Club, to_field='club_name', on_delete=models.CASCADE)
    date = models.DateTimeField('Event date', default=datetime.now)
    message = models.CharField(max_length=200, default = "none")

    def __str__(self):
        return self.message


class Student(models.Model):
    studentID = models.CharField(max_length = 9, default = 0, primary_key = True)
    schoolID = models.ForeignKey(University, to_field='schoolID', on_delete=models.CASCADE)
    UserID =  models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default = "none")
    Year_of_study = models.IntegerField(default= 0)
    major = models.CharField(max_length=200, default = "none")
    phoneNumber = models.CharField(max_length=200, default = "none")



    def __str__(self):
        return self.studentID


class ClubMember(models.Model):
    clubname = models.ForeignKey(Club, to_field='club_name', on_delete=models.CASCADE)
    studnetID = models.ForeignKey(Student, to_field='studentID', on_delete=models.CASCADE)
    MemberID = models.CharField(max_length=200, default = "none")
    

    def __str__(self):
        return self.studentID


class ClubRepresentative(models.Model):
    clubname = models.ForeignKey(Club, to_field='club_name', on_delete=models.CASCADE)
    studnetID = models.ForeignKey(Student, to_field='studentID', on_delete=models.CASCADE)
    Tresurer = models.BooleanField()
    VicePresident = models.BooleanField()
    President = models.BooleanField()


    

    def __str__(self):
        return self.studentID



class Reserves(models.Model):
    
    clubname = models.ForeignKey(Club, to_field='club_name', on_delete=models.CASCADE)
    RoomNo = models.ForeignKey(Room, to_field='RoomNo', on_delete=models.CASCADE)


    def __str__(self):
        return self.RoomNo





