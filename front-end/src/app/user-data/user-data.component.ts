import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { environment } from 'src/environments/environment';

interface UserData {
  pesel: string;
  name: string;
  job: string;
  posts: string;
  likes: string;
  followers: string;
}

@Component({
  selector: 'app-user-data',
  templateUrl: './user-data.component.html',
  styleUrls: ['./user-data.component.css']
})
export class UserDataComponent implements OnInit {

  userData: UserData = {
    pesel: "",
    name: "",
    job: "",
    posts: "",
    likes: "",
    followers: ""
  };

  constructor(
    private http: HttpClient,
    private router: Router,
    private activatedRoute: ActivatedRoute,
  ) { }

  ngOnInit(): void {
    this.loadData();
    this.activatedRoute.queryParams.subscribe(params => {
      this.userData.pesel = params['pesel'];
    });
  }

  logOut() {
    this.router.navigate(['logout']);
  }

  update() {
    this.loadData();
  }

  private loadData() {
    const endpoints = ['name', 'job', 'posts', 'likes', 'followers'];
    for (const endpoint of endpoints) {
      this.http.get<any>(`${environment.backendUrl}${endpoint}`).subscribe(
        {
          next: ((response: any) => {
            console.log(response);
            this.userData[endpoint as keyof UserData] = response[endpoint];
          }),
          error: (error => {
            console.log(error);
          })
        }
      );
    }
  }
}
