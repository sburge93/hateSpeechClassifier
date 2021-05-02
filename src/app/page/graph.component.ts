import { Component, OnInit, OnDestroy} from '@angular/core';
import {HateSpeechApiService} from '../api.service/HateSpeechApiService';
import { HateSpeechModel } from "src/models/HateSpeechModel";
import { MatCardModule } from '@angular/material/card';
import {Subscription} from 'rxjs';


@Component({
  selector: 'app-page',
  templateUrl: './graph.component.html',
  styleUrls: ['./graph.component.css']
})
export class GraphComponent implements OnInit, OnDestroy {
  hateSpeechModelSubs: Subscription;
  hateSpeechModel: HateSpeechModel;

  constructor(private hatespeechApi: HateSpeechApiService) {
  }

ngOnInit() {
    this.hateSpeechModelSubs = this.hatespeechApi
      .getHateSpeech()
      .subscribe(res => {
        console.log(res)
          this.hateSpeechModel = res;
          console.log(this.hateSpeechModel)
        },
        console.error
      );
  }

ngOnDestroy() {
    this.hateSpeechModelSubs.unsubscribe();
  }
}
