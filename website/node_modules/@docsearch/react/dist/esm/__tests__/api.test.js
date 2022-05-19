function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); enumerableOnly && (symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; })), keys.push.apply(keys, symbols); } return keys; }

function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = null != arguments[i] ? arguments[i] : {}; i % 2 ? ownKeys(Object(source), !0).forEach(function (key) { _defineProperty(target, key, source[key]); }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)) : ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } return target; }

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

function asyncGeneratorStep(gen, resolve, reject, _next, _throw, key, arg) { try { var info = gen[key](arg); var value = info.value; } catch (error) { reject(error); return; } if (info.done) { resolve(value); } else { Promise.resolve(value).then(_next, _throw); } }

function _asyncToGenerator(fn) { return function () { var self = this, args = arguments; return new Promise(function (resolve, reject) { var gen = fn.apply(self, args); function _next(value) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "next", value); } function _throw(err) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "throw", err); } _next(undefined); }); }; }

function _extends() { _extends = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; }; return _extends.apply(this, arguments); }

import { render, fireEvent, waitFor, screen, act } from '@testing-library/react';
import React from 'react';
import '@testing-library/jest-dom';
import { DocSearch as DocSearchComponent } from '../DocSearch';

function DocSearch(props) {
  return /*#__PURE__*/React.createElement(DocSearchComponent, _extends({
    appId: "woo",
    apiKey: "foo",
    indexName: "bar"
  }, props));
} // mock empty response


function noResultSearch(_queries, _requestOptions) {
  return new Promise(function (resolve) {
    resolve({
      results: [{
        hits: [],
        hitsPerPage: 0,
        nbHits: 0,
        nbPages: 0,
        page: 0,
        processingTimeMS: 0,
        exhaustiveNbHits: true,
        params: '',
        query: ''
      }]
    });
  });
}

describe('api', function () {
  beforeEach(function () {
    document.body.innerHTML = '';
  });
  it('renders with minimal parameters', function () {
    render( /*#__PURE__*/React.createElement(DocSearch, null));
    expect(document.querySelector('.DocSearch')).toBeInTheDocument();
  });
  describe('translations', function () {
    it('overrides the default DocSearchButton text', function () {
      render( /*#__PURE__*/React.createElement(DocSearch, {
        translations: {
          button: {
            buttonText: 'Recherche',
            buttonAriaLabel: 'Recherche'
          }
        }
      }));
      expect(document.querySelector('.DocSearch-Button-Placeholder').innerHTML).toBe('Recherche');
      expect(document.querySelector('.DocSearch-Button').getAttribute('aria-label')).toBe('Recherche');
    });
    it('overrides the default DocSearchModal startScreen text', /*#__PURE__*/_asyncToGenerator( /*#__PURE__*/regeneratorRuntime.mark(function _callee() {
      return regeneratorRuntime.wrap(function _callee$(_context) {
        while (1) {
          switch (_context.prev = _context.next) {
            case 0:
              render( /*#__PURE__*/React.createElement(DocSearch, {
                translations: {
                  modal: {
                    startScreen: {
                      noRecentSearchesText: 'Pas de recherche récentes'
                    }
                  }
                }
              }));
              _context.next = 3;
              return waitFor(function () {
                fireEvent.click(document.querySelector('.DocSearch-Button'));
              });

            case 3:
              expect(screen.getByText('Pas de recherche récentes')).toBeInTheDocument();

            case 4:
            case "end":
              return _context.stop();
          }
        }
      }, _callee);
    })));
    it('overrides the default DocSearchModal noResultsScreen text', /*#__PURE__*/_asyncToGenerator( /*#__PURE__*/regeneratorRuntime.mark(function _callee3() {
      return regeneratorRuntime.wrap(function _callee3$(_context3) {
        while (1) {
          switch (_context3.prev = _context3.next) {
            case 0:
              render( /*#__PURE__*/React.createElement(DocSearch, {
                transformSearchClient: function transformSearchClient(searchClient) {
                  return _objectSpread(_objectSpread({}, searchClient), {}, {
                    search: noResultSearch
                  });
                },
                translations: {
                  modal: {
                    noResultsScreen: {
                      noResultsText: 'Pas de résultats pour',
                      reportMissingResultsText: 'Ouvrez une issue sur docsearch-configs',
                      reportMissingResultsLinkText: 'Lien du repo'
                    }
                  }
                },
                getMissingResultsUrl: function getMissingResultsUrl() {
                  return 'algolia.com';
                }
              }));
              _context3.next = 3;
              return act( /*#__PURE__*/_asyncToGenerator( /*#__PURE__*/regeneratorRuntime.mark(function _callee2() {
                return regeneratorRuntime.wrap(function _callee2$(_context2) {
                  while (1) {
                    switch (_context2.prev = _context2.next) {
                      case 0:
                        _context2.next = 2;
                        return waitFor(function () {
                          fireEvent.click(document.querySelector('.DocSearch-Button'));
                        });

                      case 2:
                        fireEvent.input(document.querySelector('.DocSearch-Input'), {
                          target: {
                            value: 'q'
                          }
                        });

                      case 3:
                      case "end":
                        return _context2.stop();
                    }
                  }
                }, _callee2);
              })));

            case 3:
              expect(screen.getByText(/Pas de résultats pour/)).toBeInTheDocument();
              expect(screen.getByText(/Ouvrez une issue sur docsearch-configs/)).toBeInTheDocument();
              expect(screen.getByRole('link', {
                name: 'Lien du repo'
              })).toBeInTheDocument();

            case 6:
            case "end":
              return _context3.stop();
          }
        }
      }, _callee3);
    })));
    it('overrides the default DocSearchModal searchbox text', /*#__PURE__*/_asyncToGenerator( /*#__PURE__*/regeneratorRuntime.mark(function _callee4() {
      return regeneratorRuntime.wrap(function _callee4$(_context4) {
        while (1) {
          switch (_context4.prev = _context4.next) {
            case 0:
              render( /*#__PURE__*/React.createElement(DocSearch, {
                translations: {
                  modal: {
                    searchBox: {
                      resetButtonTitle: 'Effacer',
                      resetButtonAriaLabel: 'Effacer',
                      cancelButtonText: 'Annuler',
                      cancelButtonAriaLabel: 'Annuler'
                    }
                  }
                }
              }));
              _context4.next = 3;
              return waitFor(function () {
                fireEvent.click(document.querySelector('.DocSearch-Button'));
              });

            case 3:
              expect(document.querySelector('.DocSearch-Cancel').innerHTML).toBe('Annuler');
              expect(document.querySelector('.DocSearch-Cancel').getAttribute('aria-label')).toBe('Annuler');
              expect(document.querySelector('.DocSearch-Reset').getAttribute('title')).toBe('Effacer');
              expect(document.querySelector('.DocSearch-Reset').getAttribute('aria-label')).toBe('Effacer');

            case 7:
            case "end":
              return _context4.stop();
          }
        }
      }, _callee4);
    })));
    it('overrides the default DocSearchModal footer text', /*#__PURE__*/_asyncToGenerator( /*#__PURE__*/regeneratorRuntime.mark(function _callee5() {
      return regeneratorRuntime.wrap(function _callee5$(_context5) {
        while (1) {
          switch (_context5.prev = _context5.next) {
            case 0:
              render( /*#__PURE__*/React.createElement(DocSearch, {
                translations: {
                  modal: {
                    footer: {
                      closeText: 'Pour fermer',
                      closeKeyAriaLabel: "Touche d'échappement",
                      navigateText: 'Pour naviguer',
                      navigateUpKeyAriaLabel: 'Flèche vers le haut',
                      navigateDownKeyAriaLabel: 'Flèche le bas',
                      searchByText: 'Recherche par',
                      selectText: 'Pour selectionner',
                      selectKeyAriaLabel: "Touche d'entrée"
                    }
                  }
                }
              }));
              _context5.next = 3;
              return waitFor(function () {
                fireEvent.click(document.querySelector('.DocSearch-Button'));
              });

            case 3:
              expect(screen.getByText('Recherche par')).toBeInTheDocument();
              expect(screen.getByText('Pour fermer')).toBeInTheDocument();
              expect(screen.getByText('Pour naviguer')).toBeInTheDocument();
              expect(screen.getByText('Pour selectionner')).toBeInTheDocument();
              expect(document.querySelector('.DocSearch-Commands-Key > svg[aria-label="Touche d\'échappement"]')).toBeInTheDocument();
              expect(document.querySelector('.DocSearch-Commands-Key > svg[aria-label="Flèche vers le haut"]')).toBeInTheDocument();
              expect(document.querySelector('.DocSearch-Commands-Key > svg[aria-label="Flèche le bas"]')).toBeInTheDocument();
              expect(document.querySelector('.DocSearch-Commands-Key > svg[aria-label="Touche d\'entrée"]')).toBeInTheDocument();

            case 11:
            case "end":
              return _context5.stop();
          }
        }
      }, _callee5);
    })));
  });
  describe('getMissingResultsUrl', function () {
    it('does not render the link to the repository by default', /*#__PURE__*/_asyncToGenerator( /*#__PURE__*/regeneratorRuntime.mark(function _callee7() {
      return regeneratorRuntime.wrap(function _callee7$(_context7) {
        while (1) {
          switch (_context7.prev = _context7.next) {
            case 0:
              render( /*#__PURE__*/React.createElement(DocSearch, {
                transformSearchClient: function transformSearchClient(searchClient) {
                  return _objectSpread(_objectSpread({}, searchClient), {}, {
                    search: noResultSearch
                  });
                }
              }));
              _context7.next = 3;
              return act( /*#__PURE__*/_asyncToGenerator( /*#__PURE__*/regeneratorRuntime.mark(function _callee6() {
                return regeneratorRuntime.wrap(function _callee6$(_context6) {
                  while (1) {
                    switch (_context6.prev = _context6.next) {
                      case 0:
                        _context6.next = 2;
                        return waitFor(function () {
                          fireEvent.click(document.querySelector('.DocSearch-Button'));
                        });

                      case 2:
                        fireEvent.input(document.querySelector('.DocSearch-Input'), {
                          target: {
                            value: 'q'
                          }
                        });

                      case 3:
                      case "end":
                        return _context6.stop();
                    }
                  }
                }, _callee6);
              })));

            case 3:
              expect(screen.getByText(/No results for/)).toBeInTheDocument();
              expect(document.querySelector('.DocSearch-Help a')).not.toBeInTheDocument();

            case 5:
            case "end":
              return _context7.stop();
          }
        }
      }, _callee7);
    })));
    it('render the link to the repository', /*#__PURE__*/_asyncToGenerator( /*#__PURE__*/regeneratorRuntime.mark(function _callee9() {
      var link;
      return regeneratorRuntime.wrap(function _callee9$(_context9) {
        while (1) {
          switch (_context9.prev = _context9.next) {
            case 0:
              render( /*#__PURE__*/React.createElement(DocSearch, {
                transformSearchClient: function transformSearchClient(searchClient) {
                  return _objectSpread(_objectSpread({}, searchClient), {}, {
                    search: noResultSearch
                  });
                },
                getMissingResultsUrl: function getMissingResultsUrl(_ref9) {
                  var query = _ref9.query;
                  return "https://github.com/algolia/docsearch/issues/new?title=".concat(query);
                }
              }));
              _context9.next = 3;
              return act( /*#__PURE__*/_asyncToGenerator( /*#__PURE__*/regeneratorRuntime.mark(function _callee8() {
                return regeneratorRuntime.wrap(function _callee8$(_context8) {
                  while (1) {
                    switch (_context8.prev = _context8.next) {
                      case 0:
                        _context8.next = 2;
                        return waitFor(function () {
                          fireEvent.click(document.querySelector('.DocSearch-Button'));
                        });

                      case 2:
                        fireEvent.input(document.querySelector('.DocSearch-Input'), {
                          target: {
                            value: 'q'
                          }
                        });

                      case 3:
                      case "end":
                        return _context8.stop();
                    }
                  }
                }, _callee8);
              })));

            case 3:
              expect(screen.getByText(/No results for/)).toBeInTheDocument();
              link = document.querySelector('.DocSearch-Help a');
              expect(link).toBeInTheDocument();
              expect(link.getAttribute('href')).toBe('https://github.com/algolia/docsearch/issues/new?title=q');

            case 7:
            case "end":
              return _context9.stop();
          }
        }
      }, _callee9);
    })));
  });
});