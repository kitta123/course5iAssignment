import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FocusService {

  constructor(private _http: HttpClient) { }

  PriceList():Observable<any>{
    return this._http.get('http://127.0.0.1:5000/postprice');
  }

}
