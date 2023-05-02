import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-data',
  templateUrl: './data.component.html',
  styleUrls: ['./data.component.css']
})
export class DataComponent implements OnInit{

  textLabel = 'Hello Angular! Data Component';
  disable = false;

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    console.log("DataComponent")

    // GET request
    this.http.get<any>(environment.backendUrl + "data").subscribe(
      {
          next: ((response: any) => {
            console.log(response)
          }),
          error: (error => {
            console.log(error)
          })
      }
    )

    // POST request
    const email = { email: 'angular.fastapi@gmail.com' }
    const body = JSON.stringify(email)
    this.http.post<any>(environment.backendUrl + "data",body, {
      headers: {'Content-type': 'application/json'}
    }).subscribe(
      {
        next: ((response: any) => {
          console.log(response)
        }),
        error: (error => {
          console.log(error)
        })
      }
    )
  }

  changeTextLabel(): void {
    this.textLabel = 'Text Label has been changed! Great!'
  }

  changeButtonEnable(): void {
    this.disable = !this.disable
  }

}
