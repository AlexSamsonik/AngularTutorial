import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-data',
  templateUrl: './data.component.html',
  styleUrls: ['./data.component.css']
})
export class DataComponent implements OnInit {

  textLabel = 'Hello Angular! Data Component';
  disable = false;

  constructor() { }

  ngOnInit(): void {
  }

  changeTextLabel(): void {
    this.textLabel = 'Text Label has been changed! Great!'
  }

  changeButtonEnable(): void {
    this.disable = !this.disable
  }

}
