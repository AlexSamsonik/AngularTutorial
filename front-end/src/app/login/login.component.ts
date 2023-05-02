import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router'

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit{

  pesel = "";

  constructor(private router: Router){}

  ngOnInit(): void {
    
  }

  openUserDataPage() {
    this.router.navigate(["userdata"], {queryParams: {pesel: this.pesel}})
  }

}
