import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-user-data',
  templateUrl: './user-data.component.html',
  styleUrls: ['./user-data.component.css']
})
export class UserDataComponent implements OnInit{

  pesel = "";
  name = "";
  job = "";
  posts = "";
  likes = "";
  followers = ""

  constructor(
    private http: HttpClient,
    private router: Router,
    private activetedRoute: ActivatedRoute,
  ){}

  ngOnInit(): void {

    this.http.get<any>(environment.backendUrl + "name").subscribe(
      {
        next: ((response: any) => {
          console.log(response)
          this.name = response.name
        }),
        error: (error => {
          console.log(error)
        })
      }
    )

    this.http.get<any>(environment.backendUrl + "job").subscribe(
      {
        next: ((response: any) => {
          console.log(response)
          this.job = response.job
        }),
        error: (error => {
          console.log(error)
        })
      }
    )

    this.http.get<any>(environment.backendUrl + "posts").subscribe(
      {
        next: ((response: any) => {
          console.log(response)
          this.posts = response.posts
        }),
        error: (error => {
          console.log(error)
        })
      }
    )

    this.http.get<any>(environment.backendUrl + "likes").subscribe(
      {
        next: ((response: any) => {
          console.log(response)
          this.likes = response.likes
        }),
        error: (error => {
          console.log(error)
        })
      }
    )

    this.http.get<any>(environment.backendUrl + "followers").subscribe(
      {
        next: ((response: any) => {
          console.log(response)
          this.followers = response.followers
        }),
        error: (error => {
          console.log(error)
        })
      }
    )

    this.activetedRoute.queryParams.subscribe(params => {
      this.pesel = params['pesel'];
    })
  }

  logOut() {
    this.router.navigate(['logout'])
  }

  update() {
    
    this.http.get<any>(environment.backendUrl + "posts").subscribe(
      {
        next: ((response: any) => {
          console.log(response)
          this.posts = response.posts
        }),
        error: (error => {
          console.log(error)
        })
      }
    )

    this.http.get<any>(environment.backendUrl + "likes").subscribe(
      {
        next: ((response: any) => {
          console.log(response)
          this.likes = response.likes
        }),
        error: (error => {
          console.log(error)
        })
      }
    )

    this.http.get<any>(environment.backendUrl + "followers").subscribe(
      {
        next: ((response: any) => {
          console.log(response)
          this.followers = response.followers
        }),
        error: (error => {
          console.log(error)
        })
      }
    )
  }

}
