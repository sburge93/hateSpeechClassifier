import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable} from 'rxjs';
import {catchError} from 'rxjs/operators';
import {API_URL} from 'src/app/envs';
import {HateSpeechModel} from 'src/models/HateSpeechModel';

@Injectable()
export class HateSpeechApiService {
  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete request.');
  }

  // GET list of public, future events
  getHateSpeech(): Observable<HateSpeechModel> {
    return this.http
      .get<HateSpeechModel>(`${API_URL}/hatespeech`)
      .pipe(catchError(HateSpeechApiService._handleError));
   }
}