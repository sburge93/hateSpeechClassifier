import { Component, OnInit, OnDestroy } from '@angular/core';
import {Subscription} from 'rxjs';
import {HateSpeechApiService} from './api.service/HateSpeechApiService';
import {HateSpeechModel} from 'src/models/HateSpeechModel';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Dissertation-Project';

}
