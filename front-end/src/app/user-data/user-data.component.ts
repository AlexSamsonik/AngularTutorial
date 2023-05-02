import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-user-data',
  templateUrl: './user-data.component.html',
  styleUrls: ['./user-data.component.css']
})
export class UserDataComponent implements OnInit{

  email = "";

  constructor(
    private router: Router,
    private activetedRoute: ActivatedRoute,
  ){}

  ngOnInit(): void {
    this.activetedRoute.queryParams.subscribe(params => {
      this.email = params['email'];
    })
  }

  logOut() {
    this.router.navigate(['logout'])
  }

}
